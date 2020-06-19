from aws_cdk import (
    core,
    aws_ec2 as ec2,
)

class VpccdkStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
            
        vpc = ec2.Vpc(self, "TheVPC",
            # 'cidr' configures the IP range and size of the entire VPC.
            # The IP space will be divided over the configured subnets.
            cidr="172.17.0.0/16",
        
            # 'maxAzs' configures the maximum number of availability zones to use
            max_azs=3,
            
            enable_dns_hostnames=True,
            enable_dns_support=True,
        
            # 'subnetConfiguration' specifies the "subnet groups" to create.
            # Every subnet group will have a subnet for each AZ, so this
            # configuration will create `3 groups × 3 AZs = 9` subnets.
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    # 'subnetType' controls Internet access, as described above.
                    subnet_type=ec2.SubnetType.PUBLIC,
            
                    # 'name' is used to name this particular subnet group. You will have to
                    # use the name for subnet selection if you have more than one subnet
                    # group of the same type.
                    name="public",
            
                    # 'cidrMask' specifies the IP addresses in the range of of individual
                    # subnets in the group. Each of the subnets in this group will contain
                    # `2^(32 address bits - 24 subnet bits) - 2 reserved addresses = 254`
                    # usable IP addresses.
                    #
                    # If 'cidrMask' is left out the available address space is evenly
                    # divided across the remaining subnet groups.
                    cidr_mask=24), 
                ec2.SubnetConfiguration(
                    cidr_mask=24,
                    name="Application",
                    subnet_type=ec2.SubnetType.PRIVATE), 
                ec2.SubnetConfiguration(
                    cidr_mask=28,
                    name="Database",
                    subnet_type=ec2.SubnetType.ISOLATED,
        
                    # 'reserved' can be used to reserve IP address space. No resources will
                    # be created for this subnet, but the IP range will be kept available for
                    # future creation of this subnet, or even for future subdivision.
                    reserved=True)
            ]
        )
        