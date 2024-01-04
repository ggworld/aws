import awswrangler as wr
import boto3
boto3.setup_default_session(profile_name='834657444538_Data-Engineering',region_name='eu-west-1')
df = wr.dynamodb.read_items(
    table_name="aiola-qa_flow-execution-state",allow_full_scan=True,columns=['id','createdBy,createdAt'])

#because createdBy is a dictionary 
df['contains_Tal'] = df['createdBy'].apply(lambda x: 'Tal' in x.get('givenName', ''))
df['utc_time'] = df['createdAt'].apply(lambda x: datetime.datetime.utcfromtimestamp(int(x)/1000))


df[df.contains_Tal].sort_values(by="utc_time")
