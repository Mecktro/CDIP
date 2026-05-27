SAMPLE_POLICIES = [
    {
        "policy_name": "ReadOnlyS3",
        "description": "Read-only access to S3 resources.",
        "actions": [
            "s3:GetObject",
            "s3:ListBucket"
        ],
        "resources": [
            "arn:aws:s3:::finance-data/*"
        ]
    },
    {
        "policy_name": "AdminEscalationRisk",
        "description": "A risky policy with broad IAM permissions.",
        "actions": [
            "iam:CreateUser",
            "iam:AttachUserPolicy",
            "iam:PutUserPolicy"
        ],
        "resources": [
            "*"
        ]
    }
]


def list_policies():
    return SAMPLE_POLICIES
