// 좋아/싫어
const likeBtn = document.querySelector('#likeBtn')
likeBtn.addEventListener('click', function (event) {
    axios({
        method: 'GET',
        url: `/detail/like_users/`
    })
        .then(response => {
            if (response.data.existed_user === true) {
                event.target.classList.add('bi bi-hand-thumbs-up')
                event.target.classList.remove('bi bi-hand-thumbs-down')
            }
            else {
                event.target.classList.add('bi bi-hand-thumbs-down')
                event.target.classList.remove('bi bi-hand-thumbs-up')
            }
            const likeCount = document.querySelector('#like-count')
            likeCount.innerText = response.data.likeCount
        })
})
