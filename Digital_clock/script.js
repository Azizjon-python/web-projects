function updateTimer() {
    const now = new Date();
    const hours = now.getHours();
    const minutes = now.getMinutes();
    const seconds = now.getSeconds();

    document.getElementById('hrs').textContent = String(hours).padStart(2, '0');
    document.getElementById('min').textContent = String(minutes).padStart(2, '0');
    document.getElementById('sec').textContent = String(seconds).padStart(2, '0');

    const hourProgress = 440 - (440 * (hours % 12) / 12); // 12 soat uchun progress
    const minuteProgress = 440 - (440 * minutes / 60); // 60 daqiqa uchun progress
    const secondProgress = 440 - (440 * seconds / 60); // 60 sekund uchun progress

    document.querySelectorAll('.circle-progress')[0].style.strokeDashoffset = hourProgress;
    document.querySelectorAll('.circle-progress')[1].style.strokeDashoffset = minuteProgress;
    document.querySelectorAll('.circle-progress')[2].style.strokeDashoffset = secondProgress;
}
setInterval(updateTimer, 1000);
updateTimer();
