import simulation
import ui


def main():
    """Start the virus simulation with UI and simulation loop."""
    ui.start_ui()
    simulation.sim_main()


if __name__ == "__main__":
    main()