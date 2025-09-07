from enum import Enum


class UserGroups(Enum):
    EMPLOYEE = "employee"
    MANAGER = "manager"

    @classmethod
    def choices(cls):
        return [(role.value, role.name.replace("_", " ").title()) for role in cls]
