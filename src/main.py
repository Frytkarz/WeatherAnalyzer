import argparse
import time

import src.worker as worker


def main():
    parser = argparse.ArgumentParser(description='Get historical weather data from https://english.wunderground.com/ '
                                                 'via html parsing.')
    parser.add_argument('job', help='Job to do', choices=['parse', 'open'])
    parser.add_argument('city_code', help='City code, for example EPWA for Warsaw, Poland')
    parser.add_argument('start_year', type=int, help='Start year (include)')
    parser.add_argument('end_year', type=int, help='End year (include)')

    args = parser.parse_args()
    print("Processing job...")

    if args.job == 'parse':
        worker.parse_websites(args.city_code, args.start_year, args.end_year)
    elif args.job == 'open':
        worker.open_result(args.city_code, args.start_year, args.end_year)
    else:
        print("Unknown job!")

if __name__ == "__main__":
    start_time = time.time()
    main()
    print()
    print("--- Execution finished in %s seconds ---" % (time.time() - start_time))
