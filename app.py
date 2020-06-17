#!/usr/bin/env python3

from aws_cdk import core

from vpccdk.vpccdk_stack import VpccdkStack


app = core.App()
VpccdkStack(app, "vpccdk")

app.synth()
