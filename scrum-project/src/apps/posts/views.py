from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from firebase_config.firebase_helpers import get_data, update_data, delete_data, push_data, upload_image_to_imgur
import json
from datetime import datetime


@csrf_exempt
def manage_posts(request, post_id=None):
    """Create, retrieve, update, or delete posts."""

    if request.method == "GET":
        # Fetch all posts from Firebase
        all_posts = get_data("Post")
        print("All posts:", all_posts)  # Debugging

        if not all_posts:
            return JsonResponse({"error": "No posts available"}, status=404)

        # Handle specific post request by PostID
        if post_id:
            if isinstance(all_posts, dict):  # Dictionary structure
                for key, post in all_posts.items():
                    if post.get("PostID") == post_id:
                        return JsonResponse(post, safe=False)
            return JsonResponse({"error": "Post not found"}, status=404)

        # Return all posts if no specific post_id is provided
        return JsonResponse(all_posts, safe=False)

    elif request.method == "POST":
        try:
            # Handle JSON payloads for API clients
            if request.content_type == "application/json":
                post_data = json.loads(request.body)
            else:
                post_data = request.POST.dict()  # Handle form-data
            print("Received post data:", post_data)  # Debugging
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

        # Add timestamp
        post_data["PostTimestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Handle image upload if present
        image_file = request.FILES.get("image")  # Get the image file
        if image_file:
            try:
                image_url = upload_image_to_imgur(image_file)  # Upload image to Imgur
                post_data["PostImageURL"] = image_url  # Add image URL
            except Exception as e:
                return JsonResponse({"error": f"Image upload failed: {str(e)}"}, status=500)

        # Fetch all posts
        all_posts = get_data("Post")
        if not isinstance(all_posts, dict):
            all_posts = {}

        if post_id:  # Update an existing post
            for key, post in all_posts.items():
                if post.get("PostID") == post_id:
                    update_data(f"Post/{key}", post_data)
                    return JsonResponse({"message": "Post updated successfully!"})
            return JsonResponse({"error": "Post not found for update"}, status=404)

        else:  # Create a new post
            highest_post_id = 0
            for post in all_posts.values():
                if "PostID" in post:
                    try:
                        current_post_id = int(post["PostID"].replace("PostID", ""))
                        highest_post_id = max(highest_post_id, current_post_id)
                    except ValueError:
                        continue

            # Generate new PostID
            next_post_id = highest_post_id + 1
            post_data["PostID"] = f"PostID{next_post_id}"

            # Save the new post to Firebase
            new_key = push_data("Post", post_data)
            return JsonResponse({
                "message": "Post created successfully!",
                "PostID": post_data["PostID"],
                "PostImageURL": post_data.get("PostImageURL", None),
            })

    elif request.method == "DELETE":
        # Handle post deletion
        all_posts = get_data("Post")
        print("All posts for deletion:", all_posts)  # Debugging

        if not all_posts:
            return JsonResponse({"error": "No posts available"}, status=404)

        if isinstance(all_posts, dict):
            for key, post in all_posts.items():
                if post.get("PostID") == post_id:
                    delete_data(f"Post/{key}")
                    return JsonResponse({"message": "Post deleted successfully!"})
        return JsonResponse({"error": "Post not found"}, status=404)
