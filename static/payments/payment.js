// payments/static/payments/payment.js

document.addEventListener('DOMContentLoaded', function () {
    const paymentForm = document.getElementById('paymentForm');

    if (paymentForm) {
        paymentForm.addEventListener('submit', function (e) {
            e.preventDefault();

            const formData = new FormData(paymentForm);

            fetch('/make-payment/', {
                method: 'POST',
                body: formData,
            })
                .then(response => response.json())
                .then(data => {
                    if (data.status === 'success') {
                        alert(data.message);
                        // Redirect or perform other actions after successful payment
                    } else {
                        alert('Payment failed. Please try again.');
                    }
                })
                .catch(error => console.error('Error:', error));
        });
    }
});
