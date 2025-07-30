const addItemBtn = document.getElementById("addItemBtn");
const modal = document.getElementById("modal");
const closeModal = document.getElementById("closeModal");

// Показать модальне вікно
addItemBtn.onclick = () => modal.classList.remove("hidden");

// Сховати модальне вікно
closeModal.onclick = () => modal.classList.add("hidden");