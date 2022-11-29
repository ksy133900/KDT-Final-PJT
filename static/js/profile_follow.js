const form = document.querySelector("#follow-form")
if (form) {
  const csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value
  form.addEventListener('submit', function (event) {
    event.preventDefault()
    const userId = event.target.dataset.userId

    axios({
      method: "post",
      url: `/accounts/${userId}/follow/`,
      headers: {
        'X-CSRFToken': csrf_token
      }
    })
    .then((response) => {
      console.log('우헤헿')
      const followersCount = response.data.followers_count
      const followingsCount = response.data.followings_count
      const isFollowed = response.data.is_followed
      const followBtn = document.querySelector('#follow-form > input[type=submit]')
      if (isFollowed === true) {
        followBtn.value = '언팔로우'
        followBtn.classList.add('btn-secondary')
        followBtn.classList.remove('btn-primary')
      } else {
        followBtn.value = '팔로우'
        followBtn.classList.add('btn-primary')
        followBtn.classList.remove('btn-secondary')
      }

      const followersCountTag = document.querySelector('#followers-count')
      const followingsCountTag = document.querySelector('#followings-count')
      followersCountTag.innerText = followersCount
      followingsCountTag.innerText = followingsCount
    })
  })
}