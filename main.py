from agent.setup import setup


def main():
    try:
        setup()
    except KeyboardInterrupt:
        print("Bye!!")


if __name__ == "__main__":
    main()
