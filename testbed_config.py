from enum import Enum

SENTINEL_DOCK_ID = 0

# Port that the flask server should use
PORT = 8889
 
# This is the base URL of the AMR offboard infrastructure (backend) REST API
AMR_OFFBOARD_INFRA_REST_API_BASE_URL = "http://192.168.0.46:8000"

# This is the URL to the executor server that sends tasks requests and accepts task completion responses
TESTBED_EXECUTOR_SERVER_URL = ""

# A work cell is a physical location in the factory where a robot can be assigned to perform a task
class WorkCell(Enum):
    UNDEFINED = 0
    INSPECTION = 6
    ROBOT_ARM_1 = 1
    ROBOT_ARM_2 = 2
    DEPOT = 4
    ROBOT_ARM_3 = 5
    STAY_WHERE_IT_IS = 100  # This is a special value that is not a part of the backend enum


# An AMR is an autonomous mobile robot. We currently have the following 2 robots at the testbed
class AMR(Enum):
    AMR_1 = 1
    AMR_2 = 2

class TaskStatus(Enum):
    BACKLOG = 1
    ENQUEUED = 2
    RUNNING = 3
    COMPLETED = 4
    FAILED = 5
    CANCELED = 6


# Maps to parse json requests from the executor
parse_location_name_to_enum = {
    "Robot-Arm-1": WorkCell.ROBOT_ARM_1,
    "Robot-Arm-2": WorkCell.ROBOT_ARM_2,
    "Inspect": WorkCell.INSPECTION,
    "Depot": WorkCell.DEPOT,
}

parse_amr_resource_name_to_enum = {
    "amr1": AMR.AMR_1,
    "amr2": AMR.AMR_2,
}
