import os
from supabase import create_client, Client

url: str = os.environ.get("https://feyavqhbyfmodqldfcrq.supabase.co")
key: str = os.environ.get("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZleWF2cWhieWZtb2RxbGRmY3JxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDIxMzY0NDUsImV4cCI6MjAxNzcxMjQ0NX0.qd8ji1PEnnLtlfVN4UISVmSXaYQGBokHZEa5ZPCDGf0")
supabase: Client = create_client(url, key)


#response = supabase.table('countries').select("*").execute()