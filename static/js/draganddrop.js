let dropArea = document.getElementById("drop-area");
['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
    dropArea.addEventListener(eventName, preventDefaults, false)
    document.body.addEventListener(eventName, preventDefaults, false)
})

;
['dragenter', 'dragover'].forEach(eventName => {
    dropArea.addEventListener(eventName, highlight, false)
})

;
['dragleave', 'drop'].forEach(eventName => {
    dropArea.addEventListener(eventName, unhighlight, false)
})

dropArea.addEventListener('drop', handleDrop, false)

function preventDefaults(e) {
    e.preventDefault()
    e.stopPropagation()
}

function highlight(e) {
    dropArea.classList.add('highlight')
}

function unhighlight(e) {
    dropArea.classList.remove('active')
}

function handleDrop(e) {
    var dt = e.dataTransfer
    var files = dt.files

    handleFiles(files)
}

let uploadProgress = []
let progressBar = document.getElementById('progress-bar')

function initializeProgress(numFiles) {
    progressBar.value = 0
    uploadProgress = []

    for (let i = numFiles; i > 0; i--) {
        uploadProgress.push(0)
    }
}

function updateProgress(fileNumber, percent) {
    uploadProgress[fileNumber] = percent
    let total = uploadProgress.reduce((tot, curr) => tot + curr, 0) / uploadProgress.length
    progressBar.value = total
}

function handleFiles(files) {
    files = [...files]
    initializeProgress(files.length)
    previewFile(files[0])
    uploadFile(files[0])
    // files.forEach(uploadFile)
    // files.forEach(previewFile)
}

function previewFile(file) {
    let reader = new FileReader()
    reader.readAsDataURL(file)
    reader.onloadend = function () {
        let img = document.createElement('img')
        img.src = reader.result
        document.getElementById('gallery').appendChild(img)
    }
}

function uploadFile(file, i) {
    console.log("upload file")
    var process = document.getElementById("home-process")
    var details = document.getElementById("home-details")
    var progress = document.getElementById("home-process-progressing")
    var image = document.getElementById("home-process-image")
    var download = document.getElementById("home-process-download")
    process.style.display = "block"
    details.style.display = "none"
    image.style.display = "none"
    download.style.display = "none"

    const formData = new FormData();
    formData.append("image", file);

    axios.post('/api-bgremover/image/upload/', formData, {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        }).then(response => {
            progress.style.display = "none"
            image.style.display = "block"
            download.style.display = "block"
            image.src = response.data.response
            download.href = response.data.response
        })
        .then(error => {
            console.log(error)
        })
}