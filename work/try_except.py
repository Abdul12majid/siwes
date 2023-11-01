#try and except
import requests
import json

def get_api_data(url):
  """Gets data from the given API URL.

  Args:
    url: The URL of the API endpoint.

  Returns:
    A Python dictionary containing the API response data.
  """

  try:
    response = requests.get(url)
  except requests.exceptions.RequestException as e:
    raise Exception(f"Failed to get API data: {e}")

  if response.status_code != 200:
    raise Exception(f"API returned error code: {response.status_code}")

  try:
    data = json.loads(response.content)
  except json.JSONDecodeError as e:
    raise Exception(f"Failed to decode API response as JSON: {e}")

  return data


def main():
  """Gets and prints the data from the Hacker News API."""

  url = "https://hacker-news.firebaseio.com/v0/topstories.json"

  try:
    data = get_api_data(url)
  except Exception as e:
    print(f"Failed to get Hacker News data: {e}")
    return

  for story_id in data[:10]:
    story_url = f"https://news.ycombinator.com/item?id={story_id}"

    try:
      story_data = get_api_data(story_url)
    except Exception as e:
      print(f"Failed to get Hacker News story data for story ID {story_id}: {e}")
      continue

    story_title = story_data["title"]
    story_score = story_data["score"]

    print(f"{story_title} ({story_score})")


if __name__ == "__main__":
  main()
