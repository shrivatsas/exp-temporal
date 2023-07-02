from dataclasses import dataclass

task_queue_name = "email_subscription"


@dataclass
class WorkflowOptions:
    email: str


@dataclass
class EmailDetails:
    email: str = ""
    message: str = ""
