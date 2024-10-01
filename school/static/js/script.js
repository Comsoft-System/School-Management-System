document.addEventListener("DOMContentLoaded", function () {
    const formSteps = document.querySelectorAll(".form-step");
    let currentStep = 0;

    // Function to show the current step
    function showStep(step) {
        formSteps.forEach((formStep, index) => {
            if (index === step) {
                formStep.classList.add("form-step-active");
            } else {
                formStep.classList.remove("form-step-active");
            }
        });
    }

    // Function to validate current step
    function validateStep() {
        let isValid = true;
        const inputs = formSteps[currentStep].querySelectorAll("input[required], select[required]");

        inputs.forEach(input => {
            const errorContainer = input.nextElementSibling;
            if (!input.value.trim()) {
                input.classList.add("is-invalid");
                if (errorContainer && errorContainer.classList.contains('text-danger')) {
                    errorContainer.textContent = 'This field is required';
                }
                isValid = false;
            } else {
                input.classList.remove("is-invalid");
                if (errorContainer && errorContainer.classList.contains('text-danger')) {
                    errorContainer.textContent = '';
                }
            }
        });

        return isValid;
    }

    // Show the first step
    showStep(currentStep);

    // Handle "Next" button clicks
    document.querySelectorAll(".btn-next").forEach(button => {
        button.addEventListener("click", function () {
            if (validateStep()) {
                currentStep++;
                showStep(currentStep);
            }
        });
    });

    // Handle "Previous" button clicks
    document.querySelectorAll(".btn-prev").forEach(button => {
        button.addEventListener("click", function () {
            currentStep--;
            showStep(currentStep);
        });
    });
});
