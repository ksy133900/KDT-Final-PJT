// const books = [
//   {
//     id: 1,
//     name: '꽃을 든 남자',
//     genre: '공포',
//     url: '/../../../static/images/profile_icon.jpg'
//   },
//   {
//     id: 2,
//     name: '블랙말랑카우',
//     genre: '추리',
//     url: '/../../../static/images/profile_icon.jpg'
//   },
//   {
//     id: 3,
//     name: '페퍼민트초코',
//     genre: '로맨스',
//     url: '/../../../static/images/profile_icon.jpg'
//   },
//   {
//     id: 4,
//     name: 'z타락파워전사z',
//     genre: '판타지',
//     url: '/../../static/images/profile_icon.jpg'
//   },
//   {
//     id: 5,
//     name: '국방무늬토기',
//     genre: '판타지',
//     url: '/../../static/images/profile_icon.jpg'
//   },
//   {
//     id: 6,
//     name: '토끼공듀',
//     genre: '판타지',
//     url: '/../../static/images/profile_icon.jpg'
//   },
//   {
//     id: 7,
//     name: '남자4',
//     genre: '판타지',
//     url: '/../../static/images/bar1.png'
//   },
//   {
//     id: 8,
//     name: '여자4',
//     genre: '판타지',
//     url: '/../../static/images/bar2.png'
//   },
// ];


// const list = document.getElementById('list');

// function showList(val = '') {
//   list.innerHTML = '';
//   const res = books.forEach(book => {
//     if (book.name.includes(val)) {
//       const col = document.createElement('col');
//       col.innerHTML = `
//       <div class="card mb-3" style="max-width: 540px;">
//       <div class="row g-0" style="border: 3px solid green;">

//         <div class="col-md-5" style=" width: 100%;
//         max-width: 230px; height: 227px;">
//           <img src='${book.url}' alt='${book.name}'style="width: 100%;
//           max-width: 180px;
//           margin: 30px;">
//           <p style="font-weight: bolder; text-align: center; font-size: 25px; margin-left: 20px; margin-top: -10px;">${book.name}</p>
//         </div>
//         <div class="col-md-7" style="width: 100%;
//         max-width: 300px;">
//           <div class="card-body" style="margin-top: 20px;">
//             <p class="card-text">${book.genre} 선호</p>
//             <p class="card-text">선호 나이 </p>
//             <p class="card-text">활동 지역<br>
//               <small class="text-muted"> (정보불러오는곳)</small>
//             </p>
//             <p class="card-text">팔로워or매너지수<small class="text-muted"> (수치 불러오는곳)</small></p>
//             <button class="w-btn-neon2" style="z-index: 1; margin-left: 15%; width: 100%; max-width: 200px;" type="button" href="#">
//             리뷰 보기
//             </button>
//           </div>
//         </div>
//       </div>
//       <img src='/../../static/images/branch.png' alt:"" style="    width: 100%;
//       max-width: 40px;
//       position: absolute;
//       margin-left: 480px;
//       margin-top: 10px;"></img>
//     </div>
//       ` //이미지에 프로필
//       list.appendChild(col);
//     }
//   })
// }

// showList('');

//연관검색어
const searchFilter = (data, keyword) => {

  return data.filter((item) => (item.name.indexOf(keyword) != -1));
};

const conatiner = document.querySelector(".container_");
conatiner.style.display = 'none';
conatiner.innerHTML = books.map((book) => `<li>${book.name}</li>`).slice(0, 5).join('')

const input = document.querySelector(".search-txt");
input.addEventListener("keyup", (e) => {
  const keyword = e.target.value;
  const filterdbooks = searchFilter(books, keyword);
  conatiner.innerHTML = filterdbooks.map((book) => `<li>${book.name}</li>`).slice(0, 5).join('')
});


//연관검색어 끝

const searchInput = document.getElementById('search');
const searchBtn = document.getElementById('searchBtn');

searchBtn.addEventListener('click', (e) => {
  e.preventDefault();
  const val = searchInput.value;

  showList(val);
})
const form_ = document.getElementsByClassName('container_')[0];

searchInput.addEventListener('focusin', (event) => {
  form_.style.display = 'block';
});

searchInput.addEventListener('focusout', (event) => {
  form_.style.display = 'none';
});


//<card>
//<img src='${book.url}' alt='${book.name}'>
//</card>
//<info>
//<p> ${book.name}</p>
//<p>${book.genre} 선호</p>
//<div class="text-center mt-3 mb-3">
//<button class="w-btn-neon2" type="button" href="#">
//  리뷰 보기
//</button>
//</div>
//</info>

