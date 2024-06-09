document.addEventListener('DOMContentLoaded', function() {
    const openScheduleBtn = document.getElementById('openSchedule');
    const scheduleModal = document.getElementById('scheduleModal');
    const closeModalBtn = scheduleModal.querySelector('.close');
  
    openScheduleBtn.addEventListener('click', function(event) {
      event.preventDefault(); // Предотвращаем переход по ссылке
      scheduleModal.style.display = 'block';
    });
  
    closeModalBtn.addEventListener('click', function() {
      scheduleModal.style.display = 'none';
    });
  
    window.addEventListener('click', function(event) {
      if (event.target == scheduleModal) {
        scheduleModal.style.display = 'none';
      }
    });
  });
  