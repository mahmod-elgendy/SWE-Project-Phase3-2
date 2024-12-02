class UserProfileSerializer:
    """Serializer for user profiles."""
    def serialize(self, user_data):
        return {
            "UserName": user_data.get("UserName"),
            "UserEmail": user_data.get("UserEmail"),
            "UserBio": user_data.get("UserBio"),
            "UserCV": user_data.get("UserCV"),
            "UserPFP": user_data.get("UserPFP"),
            "UserTags": user_data.get("UserTags", []),
            "UserAccess": user_data.get("UserAccess"),
            "UserNfollowers": user_data.get("UserNfollowers", 0),
            "UserNfollowing": user_data.get("UserNfollowing", 0),
        }
