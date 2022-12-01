const books = [
  {
    id: 1,
    name: '세계문학',
    genre: '공포',
    url: '/../../../static/images/1.jpg'
  },
  {
    id: 2,
    name: '우리문학',
    genre: '추리',
    url: '/../../../static/images/2.jpg'
  },
  {
    id: 3,
    name: '죽음문학',
    genre: '로맨스',
    url: '/../../../static/images/3.jpg'
  },
  {
    id: 4,
    name: '환상문학',
    genre: '판타지',
    url: '/../../static/images/4.jpg'
  },
];


const list = document.getElementById('list');

function showList(val = '') {
  list.innerHTML = '';
  const res = books.forEach(book => {
    if (book.name.includes(val)) {
      const li = document.createElement('li');
      li.innerHTML = `
        <img src='${book.url}' alt='${book.name}'>
        <p>이름: ${book.name}</p>
        <p>장르: ${book.genre}</p>
      `
      list.appendChild(li);
    }
  })
}

showList('');


const searchFilter = (data, keyword) => {

  return data.filter((item) => (item.name.indexOf(keyword) != -1));
};

const conatiner = document.querySelector(".container");
conatiner.style.display = 'none';
conatiner.innerHTML = books.map((book) => `<li>${book.name}</li>`).join("");

const input = document.querySelector(".search-txt");
input.addEventListener("keyup", (e) => {
  const keyword = e.target.value;
  const filterdbooks = searchFilter(books, keyword);
  conatiner.innerHTML = filterdbooks
    .map((book) => `<li>${book.name}</li>`)
    .join("");
});



const searchInput = document.getElementById('search');
const searchBtn = document.getElementById('searchBtn');

searchBtn.addEventListener('click', (e) => {
  e.preventDefault();
  window.location.href = "/matching/" + "?" + "q=" + searchInput.value;
  const val = searchInput.value;
  console.log(val);
  showList(val);
})
const form_ = document.getElementsByClassName('container')[0];

searchInput.addEventListener('focusin', (event) => {
  form_.style.display = 'initial';
});

searchInput.addEventListener('focusout', (event) => {
  form_.style.display = 'none';
});