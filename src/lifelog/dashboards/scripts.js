// Example countdown function
function startCountdown(id, endDate) {
    const timerElement = document.getElementById(id);
    function updateTimer() {
        const now = new Date().getTime();
        const distance = endDate - now;

        if (distance < 0) {
            timerElement.innerHTML = "EXPIRED";
            timerElement.parentElement.classList.add('expiring-soon');
            return;
        }

        const days = Math.floor(distance / (1000 * 60 * 60 * 24));
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);

        timerElement.innerHTML = `${days}d ${hours}h ${minutes}m ${seconds}s`;

        if (distance < 86400000) { // Less than 24 hours
            timerElement.parentElement.classList.add('expiring-soon');
        }
    }

    updateTimer();
    setInterval(updateTimer, 1000);
}

// Set your countdown dates here
const moveOutDate = new Date('2025-07-30T
