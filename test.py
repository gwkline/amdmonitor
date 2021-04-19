def main():
    
   # proxies = []
    with open ('proxies.txt', 'r') as f:
        proxies = [line.strip() for line in f]

    print(proxies)

if __name__ == "__main__":
    main()
