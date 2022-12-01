const books = [
  {
    id: 1,
    name: '남자1',
    genre: '공포',
    url: '/../../../static/images/profile_icon.jpg'
  },
  {
    id: 2,
    name: '여자1',
    genre: '추리',
    url: '/../../../static/images/profile_icon.jpg'
  },
  {
    id: 3,
    name: '남자2',
    genre: '로맨스',
    url: '/../../../static/images/profile_icon.jpg'
  },
  {
    id: 4,
    name: '여자2',
    genre: '판타지',
    url: '/../../static/images/profile_icon.jpg'
  },
  {
    id: 5,
    name: '남자3',
    genre: '판타지',
    url: '/../../static/images/profile_icon.jpg'
  },
  {
    id: 6,
    name: '여자3',
    genre: '판타지',
    url: '/../../static/images/profile_icon.jpg'
  },
  {
    id: 7,
    name: '남자4',
    genre: '판타지',
    url: '/../../static/images/profile_icon.jpg'
  },
  {
    id: 8,
    name: '여자4',
    genre: '판타지',
    url: '/../../static/images/profile_icon.jpg'
  },
];


const list = document.getElementById('list');

function showList(val = '') {
  list.innerHTML = '';
  const res = books.forEach(book => {
    if (book.name.includes(val)) {
      const li = document.createElement('li');
      li.innerHTML = `
        <card>
          <img src='${book.url}' alt='${book.name}'>
        </card>  
        <info>
          <p> ${book.name}</p>
          <p>${book.genre} 선호</p>
          <div class="text-center mt-3 mb-3">
          <button class="w-btn-neon2" type="button" href="#">
            리뷰 보기
          </button>
        </div>
        </info>
      ` //이미지에 프로필
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