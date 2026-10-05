function escapeHtml(unsafe) {
    return (unsafe || "").toString()
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
}


async function fetchEducations(query = "") {
    const container = document.getElementById("educationContainer");

    if (!container) return;

    container.innerHTML = `
        <p>Memuat data...</p>
    `;

    try {
        const res = await fetch(
            "/education/json/?search=" + encodeURIComponent(query)
        );

        if (!res.ok) {
            throw new Error("Gagal mengambil data.");
        }

        const data = await res.json();

        if (data.length === 0) {
            container.innerHTML = `
                <p>Belum ada riwayat pendidikan.</p>
            `;
            return;
        }

        let htmlString = "";

        data.forEach(item => {
            htmlString += `
                <div class="education-card">
                    <h3>${escapeHtml(item.school)}</h3>
                    <p>${escapeHtml(item.degree)}</p>

                    <p>
                        ${item.is_starred ? "★" : "☆"}
                        ${escapeHtml(item.stars_count)} Star
                    </p>

                    ${
                        item.can_delete
                            ? `<button onclick="deleteEducation(${item.id})">
                                Hapus
                              </button>`
                            : ""
                    }
                </div>
            `;
        });

        container.innerHTML = htmlString;

    } catch (error) {
        container.innerHTML = `
            <p>Gagal memuat data.</p>
        `;

        console.error("Error:", error);
    }
}


async function deleteEducation(id) {
    if (!confirm("Yakin ingin menghapus data ini?")) {
        return;
    }

    const csrfElement = document.querySelector(
        "[name=csrfmiddlewaretoken]"
    );

    if (!csrfElement) {
        alert("CSRF token tidak ditemukan.");
        return;
    }

    const csrfToken = csrfElement.value;

    try {
        const response = await fetch(
            "/education/delete-ajax/" + id + "/",
            {
                method: "POST",
                headers: {
                    "X-CSRFToken": csrfToken
                }
            }
        );

        const result = await response.json();

        if (response.ok) {
            fetchEducations();
        } else {
            alert(result.message || "Gagal menghapus data.");
        }

    } catch (error) {
        console.error("Error:", error);
        alert("Terjadi kesalahan jaringan.");
    }
}


function debounce(func, delay) {
    let timeoutId;

    return function (...args) {
        clearTimeout(timeoutId);

        timeoutId = setTimeout(() => {
            func.apply(this, args);
        }, delay);
    };
}


document.addEventListener("DOMContentLoaded", () => {

    const searchInput = document.getElementById("searchInput");
    const eduForm = document.getElementById("educationForm");

    // Search dengan debounce
    if (searchInput) {
        const debouncedSearch = debounce(
            (e) => fetchEducations(e.target.value),
            400
        );

        searchInput.addEventListener("input", debouncedSearch);
    }


    // Add Education dengan AJAX
    if (eduForm) {
        eduForm.addEventListener("submit", async (e) => {
            e.preventDefault();

            const formData = new FormData(eduForm);

            try {
                const response = await fetch(
                    "/education/add-ajax/",
                    {
                        method: "POST",
                        body: formData,
                    }
                );

                const result = await response.json();

                if (response.status === 201) {

                    closeModal();

                    fetchEducations();

                    if (typeof showToast === "function") {
                        showToast(
                            "Education berhasil ditambahkan!",
                            "success"
                        );
                    }

                } else {

                    if (typeof showToast === "function") {
                        showToast(
                            result.message || "Gagal menambahkan data.",
                            "error"
                        );
                    } else {
                        alert(
                            result.message || "Gagal menambahkan data."
                        );
                    }
                }

            } catch (error) {

                console.error("Error:", error);

                if (typeof showToast === "function") {
                    showToast(
                        "Terjadi kesalahan jaringan.",
                        "error"
                    );
                } else {
                    alert("Terjadi kesalahan jaringan.");
                }
            }
        });
    }


    // Load data pertama kali
    fetchEducations();
});


function openModal() {
    const modal = document.getElementById("educationModal");

    if (modal) {
        modal.classList.remove("hidden");
    }
}


function closeModal() {
    const modal = document.getElementById("educationModal");

    if (modal) {
        modal.classList.add("hidden");
    }

    const eduForm = document.getElementById("educationForm");

    if (eduForm) {
        eduForm.reset();
    }
}