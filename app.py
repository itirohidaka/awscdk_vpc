#!/usr/bin/env python3

from aws_cdk import core

from vpccdk.vpccdk_stack_east import VpccdkStack as east1
from vpccdk.vpccdk_stack_west import VpccdkStack as west1

import os

app = core.App()

env_east=core.Environment(account=os.environ["CDK_DEFAULT_ACCOUNT"], region="us-east-1")
env_west=core.Environment(account=os.environ["CDK_DEFAULT_ACCOUNT"], region="us-west-1")

east1(app, "vpccdk-east", env=env_east)
west1(app, "vpccdk-west", env=env_west)

app.synth()
