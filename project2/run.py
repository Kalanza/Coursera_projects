#!/usr/bin/env python3

import os
import requests

def main():
    # Configuration
    BASEPATH = '/home/kalanza/Coursera_projects/project2/'
    API_URL = 'http://34.139.64.219/feedback/'
    
    # Validate base directory exists
    if not os.path.isdir(BASEPATH):
        raise FileNotFoundError(f"Directory not found: {BASEPATH}")

    # Get list of files in directory
    try:
        files = os.listdir(BASEPATH)
    except PermissionError:
        raise PermissionError(f"Permission denied accessing: {BASEPATH}")

    feedback_list = []

    # Process each file
    for filename in files:
        filepath = os.path.join(BASEPATH, filename)
        
        # Skip directories, only process files
        if not os.path.isfile(filepath):
            continue
            
        # Skip non-text files (optional)
        if not filename.lower().endswith('.txt'):
            continue

        try:
            with open(filepath, 'r') as f:
                # Read file content and create feedback dictionary
                feedback = {
                    "title": f.readline().rstrip("\n"),
                    "name": f.readline().rstrip("\n"),
                    "date": f.readline().rstrip("\n"),
                    "feedback": f.read().rstrip("\n")
                }
                feedback_list.append(feedback)
                print(f"Processed: {filename}")
                
        except IOError as e:
            print(f"Error processing {filename}: {str(e)}")
            continue

    # Post feedback to API
    for item in feedback_list:
        try:
            resp = requests.post(API_URL, json=item)
            
            if resp.status_code == 201:
                print(f"Successfully posted feedback. ID: {resp.json().get('id')}")
            else:
                print(f"Failed to post feedback. Status: {resp.status_code}, Response: {resp.text}")
                
        except requests.exceptions.RequestException as e:
            print(f"API Error: {str(e)}")
            continue

if __name__ == '__main__':
    main()