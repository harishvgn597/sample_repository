// Define the Vue app
new Vue({
    el: '#app',
    data: {
      seats: [],
    },
    created() {
      // Generate 50 seats
      for (let i = 1; i <= 50; i++) {
        this.seats.push({ id: 'Seat ' + i, selected: false, booked: false });
      }
    },
    methods: {
      toggleSeat(seatId) {
        const seat = this.seats.find(s => s.id === seatId);
        seat.selected = !seat.selected; // Toggle the selection
      },
      bookSeats() {
        const selectedSeats = this.seats.filter(seat => seat.selected).map(seat => seat.id);
        // Send selectedSeats to the backend using an API call or perform any other action here
        console.log('Selected Seats:', selectedSeats);
        // Reset selected seats to false after booking
        this.seats.forEach(seat => seat.selected = false);
      }
    }
  });
  