Echo
====

A very simple plugin that will respond to query/commands with the same text that was used to initiate the interaction.

Primary used for testing purposes.

## Installation

Can be easily installed through the Web UI by using [Web UI Plugins](https://github.com/edouardpoitras/eva-web-ui-plugins).

Alternatively, add `echo` to your `eva.conf` file in the `enabled_plugins` option list and restart Eva.

## Usage

Echo has a very low priority on the interaction trigger (-100), and so it will only be triggered when no other plugins have opted to respond to a query/command from the client.

When no output has been designated as a response and Echo gets a chance to handle the interaction, it will copy whatever is in the context's input_text variable and set that as output.

## Configuration

Default configuration options can be changed by adding a `echo.conf` file in your plugin configuration path (can be configured in `eva.conf`, but usually `~/eva/configs`).

To get an idea of what configuration options are available, you can take a look at the `echo.conf.spec` file in this repository, or use the [Web UI Plugins](https://github.com/edouardpoitras/eva-web-ui-plugins) plugin and view them at `/plugins/configuration/echo`.

Here is a breakdown of the available options:

    echo_prefix
        Type: String
        Default: ''
        Here you can set text that will appear before every response from the echo plugin.
