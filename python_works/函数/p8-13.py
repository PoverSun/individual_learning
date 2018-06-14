def build_profile(first,last,**user_info):
    """创建一个字典，其中包含我们知道用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('潘','晓冬',sex='男',field='宁夏大学',age=23)

print(user_profile)