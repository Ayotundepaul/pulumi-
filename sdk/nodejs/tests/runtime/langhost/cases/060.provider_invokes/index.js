// Test the ability to invoke provider functions via RPC.

let assert = require("assert");
let pulumi = require("../../../../../");
let semver = require("semver");

class Provider extends pulumi.ProviderResource {
    constructor(name, opts) {
        super("test", name, {}, opts);
    }
}

const provider = new Provider("p");

let args = {
    a: "hello",
    b: true,
    c: [0.99, 42, { z: "x" }],
    id: "some-id",
    urn: "some-urn",
};

let result2 = pulumi.runtime.invoke("test:index:echo", args, { provider });
result2.then((v) => {
    assert.deepStrictEqual(v, args);
});
