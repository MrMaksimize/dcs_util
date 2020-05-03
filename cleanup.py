from dcs_util.clients import *
from dcs_util.firehose_helpers import *
from dcs_util.lambda_helpers import *
from dcs_util.iam_helpers import *
from dcs_util.s3_helpers import *

print("Cleanup Runtime")
clean_buckets()
clean_roles()
clean_lambdas()
clean_streams()
