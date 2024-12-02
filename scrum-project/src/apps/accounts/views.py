from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from firebase_config.firebase_helpers import get_data, update_data, delete_data
import json  # For handling JSON data in POST requests

@csrf_exempt
def manage_profile(request, user_id):
    """View, update, or delete a user profile."""
    if request.method == "GET":
        # Retrieve all users from Firebase
        all_users = get_data("User")  # Fetch the full "User" table

        # Debugging: Check the structure of all_users
        print(f"Retrieved users from Firebase: {all_users}")

        # Check if the result is a dictionary (numerical keys)
        if isinstance(all_users, dict):
            for key, user in all_users.items():
                # Check if the current user's `UserID` matches the requested `user_id`
                if user.get('UserID') == user_id:
                    return JsonResponse(user, safe=False)

        # If no user is found
        return JsonResponse({"error": "User not found"}, status=404)

    elif request.method == "POST":
        try:
            # Parse JSON data from the request body
            profile_data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

        # Check for profile picture or CV URLs in the profile data
        if 'UserPFP' in profile_data:  # Profile picture URL
            # Assuming 'UserPFP' is the field for profile picture URL
            profile_data["UserPFP"] = profile_data.get('UserPFP', '')

        if 'UserCV' in profile_data:  # CV URL
            # Assuming 'UserCV' is the field for CV URL
            profile_data["UserCV"] = profile_data.get('UserCV', '')

        # Retrieve all users from Firebase
        all_users = get_data("User")  # Fetch the full "User" table

        # Check if the result is a dictionary (numerical keys)
        if isinstance(all_users, dict):
            for key, user in all_users.items():
                # Check if the current user's `UserID` matches the requested `user_id`
                if user.get('UserID') == user_id:
                    # Update the user profile with the new data (profile picture or CV URL)
                    update_data(f"User/{key}", profile_data)
                    return JsonResponse({"message": "Profile updated successfully!"})

        # If no user is found
        return JsonResponse({"error": "User not found"}, status=404)

    elif request.method == "DELETE":
        # Retrieve all users from Firebase
        all_users = get_data("User")  # Fetch the full "User" table

        # Check if the result is a dictionary (numerical keys)
        if isinstance(all_users, dict):
            for key, user in all_users.items():
                # Check if the current user's `UserID` matches the requested `user_id`
                if user.get('UserID') == user_id:
                    # Delete the user profile
                    delete_data(f"User/{key}")
                    return JsonResponse({"message": "Profile deleted successfully!"})

        # If no user is found
        return JsonResponse({"error": "User not found"}, status=404)
