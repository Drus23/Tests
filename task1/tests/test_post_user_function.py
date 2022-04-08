from task1 import post_user


def test_post_user():
    name = 'morpheus'
    job = 'leader'
    url = 'https://reqres.in/api/users'
    response = post_user(url, name, job)

    result = False
    r_json = response.json()
    if r_json['name'] == name and r_json['job'] == job:
        result = True
    assert result
