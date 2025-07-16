// Evacuation Countdown (Set your target date below)
const evacTarget = new Date("2025-07-31T23:59:59");
const evacCountdown = document.getElementById('evacCountdown');
function updateEvacCountdown() {
  const now = new Date();
  const diff = evacTarget - now;
  if (diff < 0) {
    evacCountdown.textContent = "TIME'S UP!";
    return;
  }
  const days = Math.floor(diff / (1000*60*60*24));
  const hours = Math.floor((diff/(1000*60*60))%24);
  const mins = Math.floor((diff/(1000*60))%60);
  evacCountdown.textContent = `${days}d ${hours}h ${mins}m`;
}
setInterval(updateEvacCountdown, 1000);
updateEvacCountdown();

// Placeholder for Lyft Progress (replace with real data or input logic)
document.getElementById('lyftHours').textContent = "12h 20m"; // Example

// Placeholder for Health Status & other cards
document.getElementById('healthStatus').textContent = "BP OK • HYDRATED";
document.getElementById('houseTasks').textContent = "3 Rooms To Go";
document.getElementById('ebayStats').textContent = "14 Items";
