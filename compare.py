#!/usr/bin/env python3
import json, sys, os, glob

def extract_usernames_from_json(path):
    # Handles followers_X.json and following.json structures (string_list_data)
    def walk(obj, out):
        if isinstance(obj, dict):
            if 'string_list_data' in obj and obj['string_list_data']:
                for item in obj['string_list_data']:
                    val = item.get('value')
                    if isinstance(val, str) and val:
                        out.add(val.strip().lower())
            for v in obj.values():
                walk(v, out)
        elif isinstance(obj, list):
            for el in obj:
                walk(el, out)

    usernames = set()
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    walk(data, usernames)
    return usernames

def load_followers_following(root_dir):
    # Followers: may be split across followers_1.json, followers_2.json, ...
    followers_files = sorted(glob.glob(os.path.join(root_dir, 'followers_and_following', 'followers_*.json')))
    if not followers_files:
        followers_files = sorted(glob.glob(os.path.join(root_dir, '**', 'followers_*.json'), recursive=True))

    followers = set()
    for f in followers_files:
        followers |= extract_usernames_from_json(f)

    # Following: usually following.json
    following_candidates = [
        os.path.join(root_dir, 'followers_and_following', 'following.json')
    ]
    following = set()
    for cand in following_candidates + sorted(glob.glob(os.path.join(root_dir, '**', 'following*.json'), recursive=True)):
        if os.path.exists(cand):
            following |= extract_usernames_from_json(cand)

    return followers, following

def main():
    if len(sys.argv) < 2:
        print("Usage: python compare.py /path/to/extracted/instagram-data")
        sys.exit(1)

    root = sys.argv[1]
    followers, following = load_followers_following(root)

    not_following_back = sorted(following - followers)
    fans_you_dont_follow = sorted(followers - following)

    print(f"Following: {len(following)}")
    print(f"Followers: {len(followers)}")
    print()
    print(f"Not following you back ({len(not_following_back)}):")
    for u in not_following_back:
        print(u)
    print()
    print(f"Followers you don't follow ({len(fans_you_dont_follow)}):")
    for u in fans_you_dont_follow:
        print(u)

if __name__ == '__main__':
    main()
