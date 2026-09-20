const locationInput = document.getElementById("location-input");
const statusSelect = document.getElementById("status-select");
const clearButton = document.getElementById("clear-filters");
const resultsContainer = document.getElementById("request-results");
const requestCount = document.getElementById("request-count");

let currentBloodGroup = "";


/* ========================================
   LOAD RESULTS
======================================== */

function loadRequests(page = 1) {

    const location = locationInput.value.trim();
    const status = statusSelect.value;

    const params = new URLSearchParams();

    if (currentBloodGroup) {
        params.set("blood_group", currentBloodGroup);
    }

    if (location) {
        params.set("location", location);
    }

    if (status) {
        params.set("status", status);
    }

    params.set("page", page);


    fetch(
        `/requests/?${params.toString()}`,
        {
            headers: {
                "X-Requested-With": "XMLHttpRequest"
            }
        }
    )
    .then(response => response.text())
    .then(html => {

        resultsContainer.innerHTML = html;

        updateCount();

        attachPaginationEvents();

    })
    .catch(error => {

        console.error(
            "Request filtering error:",
            error
        );

    });
}


/* ========================================
   UPDATE COUNT
======================================== */

function updateCount() {

    const cards = resultsContainer.querySelectorAll(
        ".request-card"
    );

    /*
        Count will be updated from server response
        through the URL request.
    */

    const location = locationInput.value.trim();
    const status = statusSelect.value;

    if (!location && !status && !currentBloodGroup) {
        return;
    }

    /*
        For filtered results, count visible cards.
        Pagination will still work from Django.
    */

    if (requestCount) {
        requestCount.textContent = cards.length;
    }
}


/* ========================================
   BLOOD GROUP FILTER
======================================== */

document
    .querySelectorAll(".blood-filter-btn")
    .forEach(button => {

        button.addEventListener(
            "click",
            function () {

                document
                    .querySelectorAll(".blood-filter-btn")
                    .forEach(btn => {
                        btn.classList.remove("active");
                    });

                this.classList.add("active");

                currentBloodGroup =
                    this.dataset.blood || "";

                loadRequests();

            }
        );

    });


/* ========================================
   LOCATION FILTER
======================================== */

locationInput.addEventListener(
    "input",
    function () {

        /*
            Every letter typed triggers filtering.
        */

        loadRequests();

    }
);


/* ========================================
   STATUS FILTER
======================================== */

statusSelect.addEventListener(
    "change",
    function () {

        loadRequests();

    }
);


/* ========================================
   CLEAR FILTERS
======================================== */

clearButton.addEventListener(
    "click",
    function () {

        locationInput.value = "";

        statusSelect.value = "";

        currentBloodGroup = "";

        document
            .querySelectorAll(".blood-filter-btn")
            .forEach(button => {
                button.classList.remove("active");
            });

        document
            .querySelector('.blood-filter-btn[data-blood=""]')
            .classList.add("active");

        loadRequests();

    }
);


/* ========================================
   PAGINATION
======================================== */

function attachPaginationEvents() {

    document
        .querySelectorAll(".pagination-link")
        .forEach(button => {

            button.addEventListener(
                "click",
                function () {

                    const page =
                        this.dataset.page;

                    loadRequests(page);

                    window.scrollTo({
                        top: 0,
                        behavior: "smooth"
                    });

                }
            );

        });

}

attachPaginationEvents();