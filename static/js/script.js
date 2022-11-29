const books = [
  {
    id: 1,
    name: '세계문학',
    genre: '공포',
    url: './static/images/세계문학.jpg'
  },
  {
    id: 2,
    name: '우리문학',
    genre: '추리',
    url: 'static/images/우리문학.jpg'
  },
  {
    id: 3,
    name: '죽음문학',
    genre: '로맨스',
    url: '../죽음문학.jpg'
  },
  {
    id: 4,
    name: '환상문학',
    genre: '판타지',
    url: 'static/images/환상문학.jpg'
  },
]

const list = document.getElementById('list');

function showList(val) {
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

const searchInput = document.getElementById('search');
const searchBtn = document.getElementById('searchBtn');

searchBtn.addEventListener('click', (e) => {
  e.preventDefault();
  const val = searchInput.value;
  console.log(val);
  showList(val);
})