document.getElementById('search-form').addEventListener('submit', async (event) => {
    event.preventDefault(); // Ngăn chặn hành động mặc định

    const urlInput = document.getElementById('url').value;
    
    if (!isValidURL(urlInput)) {
        alert('Vui lòng nhập một URL hợp lệ.');
        return;
    }

    const formData = new FormData(event.target);
    const response = await fetch('/scan', {
        method: 'POST',
        body: formData
    });
    const result = await response.json();
    const resultContent = document.getElementById('result-content');
    resultContent.innerHTML = `<h2>Fake News Percentage: ${result.fake_percentage.toFixed(2)}%</h2>`;
    
    if (result.fake_paragraphs.length > 0) {
        resultContent.innerHTML += "<h3>Fake Paragraphs:</h3>";
        result.fake_paragraphs.forEach((para, index) => {
            resultContent.innerHTML += `<div class="paragraph"><strong>Paragraph ${index + 1}:</strong> <p>${para}</p></div>`;
        });
    } else {
        resultContent.innerHTML += "<p>No fake news detected.</p>";
    }
    
    document.getElementById('result').classList.add('show'); // Hiển thị lớp phủ với hiệu ứng
});

function closeResult() {
    document.getElementById('result').classList.remove('show'); // Ẩn lớp phủ với hiệu ứng
}

// Thêm sự kiện nhấn Enter cho ô tìm kiếm
document.getElementById('url').addEventListener('keydown', (event) => {
    if (event.key === 'Enter') {
        event.preventDefault(); // Ngăn chặn hành động mặc định
        document.getElementById('search-form').dispatchEvent(new Event('submit')); // Gửi form
    }
});


function isValidURL(url) {
    try {
        new URL(url);
        return true;
    } catch (e) {
        return false;
    }
}