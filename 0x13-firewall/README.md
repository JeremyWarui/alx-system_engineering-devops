# 0x13. Firewall

---

> Project focusing on what if Firewall and how to configure the `ufw` with specific rules

## TASKS

**0. Block all incoming traffic but**

Configure ufw so that it blocks all incoming traffic, except the following TCP ports:
	- 22 (SSH)

	- 443 (HTTPS SSL)

	- 80 (HTTP)

`0-block_all_incoming_traffic_but` - has the configurations

**1. Port forwarding**

Configure web-01 so that its firewall redirects port 8080/TCP to port 80/TCP.

`100-port_forwarding` - has the configurations on ufw
