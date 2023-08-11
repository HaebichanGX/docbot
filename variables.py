DIRECTORY_PATH = "docs/"
PROFILE = 'default'
DATABRICKS_SAVE_PATH = 'data/final_databricks_df.csv'

import os

openai_api_key = os.environ.get('OPENAI_API_KEY')
CLUSTER_ID = os.environ.get("CLUSTER_ID")
GITHUB_API_ACCESS_TOKEN = os.environ.get("GITHUB_API_ACCESS_TOKEN")

filtered_id_list = [
    "U04RJ5CUP2S:CUTCNHN82:1679930573.582099"
]

query = '''select *, FROM_UNIXTIME(try_cast(a.ts as double)) AS datetime_column from hive_metastore.devrel_slack_events.gold_parent_messages_devrel_reaction_added as a

inner join hive_metastore.devrel_slack_events.gold_parent_messages_join_replies as r 

using (id, channel_name, ts, type, user, text, event_ts_final, is_parent_message)

WHERE a.white_check_mark_added_at is not null
AND a.channel_name = "gx-community-support"'''

