"""Perform simulation of a M/M/c queueing system using SimPy."""
import simpy
import models.simpy_m_m_c as simpy_mmc
from visualizations.performance_plots import histogram_plot, scatter_plot, percentile_plot, heatmap_plot

# Default parameters
NUM_SERVERS = 1      # Number of servers
ARRIVAL_RATE = 0.5 # Arrival rate (clients per second)
SERVICE_RATE = 1.0   # Service rate (clients per second)
SIM_DURATION = 100_000   # Duration of the simulation (seconds)

def main(num_servers=NUM_SERVERS, arrival_rate=ARRIVAL_RATE, service_rate=SERVICE_RATE, sim_duration=SIM_DURATION):
    """Run the M/M/c queue simulation.

    The function takes the number of servers, arrival rate, service duration, and simulation duration as parameters.
    It returns the mean response time and mean number of clients in the system.
    """

    # Create the SimPy environment and the server
    env = simpy.Environment()
    server = simpy.Resource(env, capacity=num_servers)

    # Create the M/M/c queueing system
    mmc_queue = simpy_mmc.SimpyQueue(env, server, arrival_rate, service_rate)

    # Start the request generator and the statistics recorder
    env.process(mmc_queue.generate_requests())
    env.process(mmc_queue.record_statistics(sampling_interval=1.0))

    # Run the simulation
    env.run(until=sim_duration)

    # Get the response time measurements
    response_times = mmc_queue.get_response_times()
    scatter_plot(response_times, filename='scatter.png')
    histogram_plot(response_times, filename='histogram.png')
    percentile_plot(response_times, filename='percentiles.png')
    heatmap_plot(response_times, filename='heatmap.png')


    # Create the different plots


if __name__ == "__main__":
    main()
