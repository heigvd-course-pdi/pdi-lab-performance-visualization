"""SimPy simulation of an M/M/c queueing system.
The system has a c server and an infinite queue.
The inter-arrival time is exponentially distributed (Poisson arrivals).
The service time is exponentially distributed.
"""

from statistics import mean
from numpy.random import exponential

# ---------------------------------------------------------------------------
class SimpyQueue:
    """Class representing an M/M/c queueing system using SimPy."""

    def __init__(self, env, server, arrival_rate, service_rate):
        """Initialize the parameters of the M/M/c queueing system and the statistics arrays."""
        self.env = env
        self.server = server
        self.interarrival_time = 1.0 / arrival_rate
        self.service_time = 1.0 / service_rate
        # Statistics
        self.response_times = []
        self.clients_in_system = []


    def generate_requests(self):
        """Generate requests following a Poisson process."""
        while True:
            interarrival_time_exp = exponential(self.interarrival_time)
            yield self.env.timeout(interarrival_time_exp)
            self.env.process(self.process_request())


    def process_request(self):
        """Place a request in the queue and process it when the server is available.
        
        The method also records statistics about the response time.
        """
        arrival_time = self.env.now

        job = self.server.request()
        yield job
        service_time_exp = exponential(self.service_time)
        yield self.env.timeout(service_time_exp)
        self.server.release(job)

        departure_time = self.env.now
        self.response_times.append(departure_time - arrival_time)


    def record_statistics(self, sampling_interval):
        """Periodically collect statistics about the number of clients in the system."""
        while True:
            yield self.env.timeout(sampling_interval)
            self.clients_in_system.append(self.server.count + len(self.server.queue))


    def compute_statistics(self):
        """Compute and return the mean response time and mean number of clients in the system."""
        mean_response_time = mean(self.response_times)
        mean_clients_in_system = mean(self.clients_in_system)
        return {'E[T]': mean_response_time, 'E[N]': mean_clients_in_system}

    def get_response_times(self):
        """Return the list of recorded response times."""
        return self.response_times

    def get_clients_in_system(self):
        """Return the list of recorded number of clients in the system."""
        return self.clients_in_system
