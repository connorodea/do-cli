
---

# DigitalOcean CLI (do-cli)

`do-cli` is a custom command-line interface for managing DigitalOcean resources. This tool leverages the `pydo` library to interact with DigitalOcean's API and provides a user-friendly CLI built with `click`.

## Features

- List and manage DigitalOcean droplets.
- Manage SSH keys (list, add, and remove).
- Create, list, and delete Kubernetes clusters.
- Manage block storage volumes.
- Fully customizable and extendable.

---

## Installation

### Prerequisites

- Python 3.7 or higher
- A valid DigitalOcean API token (get it from [DigitalOcean API Settings](https://cloud.digitalocean.com/settings/api/tokens))

---

### Clone the Repository

```bash
git clone https://github.com/<your-username>/do-cli.git
cd do-cli
```

---

### Install Dependencies

Using `pip`:
```bash
pip install -r requirements.txt
```

---

### Set Up Environment Variables

Create a `.env` file in the root directory and add your DigitalOcean API token:

```plaintext
DIGITALOCEAN_API_KEY=<your-digitalocean-api-token>
```

Alternatively, export the token as an environment variable:
```bash
export DIGITALOCEAN_API_KEY=<your-digitalocean-api-token>
```

---

## Usage

### Basic Commands

- **List Droplets**
  ```bash
  python do_cli.py list-droplets
  ```

- **Create a Droplet**
  ```bash
  python do_cli.py create-droplet
  ```

- **Delete a Droplet**
  ```bash
  python do_cli.py delete-droplet --droplet-id <droplet-id>
  ```

- **List SSH Keys**
  ```bash
  python do_cli.py list-ssh-keys
  ```

- **Add SSH Key**
  ```bash
  python do_cli.py add-ssh-key --name <key-name> --public-key <public-key>
  ```

---

## Development

### Testing

Run tests using `pytest`:

```bash
pytest
```

For integration tests, ensure your `.env` file contains a valid DigitalOcean token.

---

### Docker

To run the CLI in a Docker container:

1. **Build the Docker Image**
   ```bash
   docker build -t do-cli .
   ```

2. **Run the Container**
   ```bash
   docker run -it --rm --env-file .env do-cli list-droplets
   ```

---

## Contribution

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch.
3. Submit a pull request.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgements

- [DigitalOcean API](https://docs.digitalocean.com/reference/api/)
- [PyDo](https://github.com/digitalocean/pydo)
- [Click Documentation](https://click.palletsprojects.com/)

---
