from aws_cdk.core import Stack

from b_cfn_twilio_task_queue.function import TwilioTaskQueueSingletonFunction
from b_cfn_twilio_task_queue.resource import TwilioTaskQueueResource


class TestingInfrastructure(Stack):
    def __init__(self, scope: Stack):
        super().__init__(
            scope=scope,
            id=f'TestingStack',
            stack_name=f'TestingStack'
        )

        function = TwilioTaskQueueSingletonFunction(
            scope=self,
            name='TestingFunction',
            twilio_account_sid='Test1',
            twilio_auth_token='Test2',
            twilio_workspace_sid='Test3'
        )

        TwilioTaskQueueResource(
            scope=self,
            task_queue_function=function,
            task_queue_name='TestTaskQueue'
        )
