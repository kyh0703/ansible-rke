import yaml
import sys

cluster_data = {
    "nodes": [],
    "ignore_docker_version": False,
    "ssh_key_path": "~/.ssh/id_rsa",
    "ssh_agent_auth": False
}

# with open("./playbook.yml") as f:
#     vegetables = yaml.load(f, Loader=yaml.FullLoader)
#     print(vegetables)

def make_master(ip):
    master = dict()
    master["address"] = ip
    master["user"] = "rke"
    master["port"] = 22
    master["roles"] = ["controlplane", "etcd"]
    master["docker_socket"] = "/var/run/docker.sock"
    master["ssh_key_path"] = "~/.ssh/id_rsa"
    cluster_data["nodes"].append(master)

def make_worker(ip):
    worker = dict()
    worker["address"] = ip
    worker["user"] = "rke"
    worker["port"] = 22
    worker["roles"] = ["worker"]
    worker["docker_socket"] = "/var/run/docker.sock"
    worker["ssh_key_path"] = "~/.ssh/id_rsa"
    cluster_data["nodes"].append(worker)

def save_cluster_yml():
    with open("./cluster.yml", "w") as fw:
        yaml.dump(cluster_data, fw)

if __name__ == "__main__":
    argument = sys.argv
    del argument[0]
    make_master("100.100.103.178")
    make_worker("100.100.103.179")
    save_cluster_yml()