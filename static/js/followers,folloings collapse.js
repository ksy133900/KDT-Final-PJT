const multiCollapseExample1followings = document.querySelector('#multiCollapseExample1')
const multiCollapseExample2followers = document.querySelector('#multiCollapseExample2')


const multiCollapseExample1 = new bootstrap.Collapse('#multiCollapseExample1', {
  toggle: false
})


if (multiCollapseExample2followers) {
  const multiCollapseExample2 = new bootstrap.Collapse('#multiCollapseExample2', {
    toggle: false
  })
  multiCollapseExample1followings.addEventListener('show.bs.collapse', event => {
    multiCollapseExample2.hide()
  })
  multiCollapseExample2followers.addEventListener('show.bs.collapse', event => {
    multiCollapseExample1.hide()

  })
}
