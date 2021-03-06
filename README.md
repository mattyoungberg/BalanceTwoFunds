# BalanceTwoFunds

A Python CLI that brings balance to your portfolio, your mind, and the universe.

---

### Table of Contents

1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Examples](#examples)
    1. [Rebalance two funds, no deposit](#rebalance-two-funds-no-deposit)
    2. [Rebalance two funds with a deposit](#rebalance-two-funds-with-a-deposit)
    3. [I can't remember which one is fund one and fund two...](#i-cant-remember-which-one-is-fund-one-and-fund-two)
4. [Usage](#usage)
5. [Notes](#notes)


---
## Requirements

BalanceTwoFunds requires Python 3.6 or later.

---
## Installation

Run the following command from your terminal:

```
pip install balancetwofunds
```

Assuming Python is correctly configured on your machine, the installation process will make the CLI available from your command line.

---

## Examples

### Rebalance two funds, no deposit
Say you have $55 dollars in fund one and $45 in fund two, but you want them to be balanced 50% and 50%.

Issue the following command from your terminal:

```
balancetwofunds 55 .5 45 .5
```

Which will output the following to your terminal:

```
╒════════════════╕
│    FUND ONE    │
╞════════════════╡
│  ACTION: SELL  │
│  MOVE: -5.00   │
├────────────────┤
│ Current: 55.00 │
│ Target: 50.00  │
└────────────────┘

╒════════════════╕
│    FUND TWO    │
╞════════════════╡
│  ACTION: BUY   │
│   MOVE: 5.00   │
├────────────────┤
│ Current: 45.00 │
│ Target: 50.00  │
└────────────────┘
```

### Rebalance two funds with a deposit

Let's take the last example, but this time, instead of selling, you simply want to rebalance using a deposit or cash position. For our purposes, let's say we deposited $20.

Use the optional `-d` or `--deposit` flag to provide the program with the context:

```
balancetwofunds 55 .5 45 .5 -d 20
```

Which will output:

```
╒════════════════╕
│    FUND ONE    │
╞════════════════╡
│  ACTION: BUY   │
│   MOVE: 5.00   │
├────────────────┤
│ Current: 55.00 │
│ Target: 60.00  │
└────────────────┘

╒════════════════╕
│    FUND TWO    │
╞════════════════╡
│  ACTION: BUY   │
│  MOVE: 15.00   │
├────────────────┤
│ Current: 45.00 │
│ Target: 60.00  │
└────────────────┘
```


### I can't remember which one is fund one and fund two...

Add the `-n1` and `-n2` optional arguments to provide the program with the names of your fund:

```
balancetwofunds 55 .5 -n1 FZROX 45 .5 -n2 FXNAX -d 20
```

Which will output:

```
╒════════════════╕
│     FZROX      │
╞════════════════╡
│  ACTION: BUY   │
│   MOVE: 5.00   │
├────────────────┤
│ Current: 55.00 │
│ Target: 60.00  │
└────────────────┘

╒════════════════╕
│     FXNAX      │
╞════════════════╡
│  ACTION: BUY   │
│  MOVE: 15.00   │
├────────────────┤
│ Current: 45.00 │
│ Target: 60.00  │
└────────────────┘
```


---

## Usage

```
usage: balancewithdeposit.py [-h] [-v] [-d DEPOSIT] [-n1 FUNDONENAME]
                             [-n2 FUNDTWONAME]
                             fundOneCurrentBalance fundOneTargetPercentage
                             fundTwoCurrentBalance fundTwoTargetPercentage

A Python CLI that does the necessary math to balance two investment funds with
a new deposit.

positional arguments:
  fundOneCurrentBalance
                        The current value of the first fund to be rebalanced
  fundOneTargetPercentage
                        The desired percentage of how much the first fund
                        should contribute to the total balance between the two
                        funds
  fundTwoCurrentBalance
                        The current value of the second fund to be rebalanced
  fundTwoTargetPercentage
                        The desired percentage of how much the second fund
                        should contribute to the total balance between the two
                        funds

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -d DEPOSIT, --deposit DEPOSIT
                        An amount deposited to be accounted for the in the
                        rebalancing
  -n1 FUNDONENAME, --fundOneName FUNDONENAME
                        A name for the first fund to be used in the program
                        output
  -n2 FUNDTWONAME, --fundTwoName FUNDTWONAME
                        A name for the second fund to be used in the program
                        output
```

---

## Notes

- This program relies heavily on the `Decimal` Python standard library. It will provide up to 20 digits of precision.
- Money values will be rounded to two cents before usage in the program's math.
- Percentage values will take whatever precision you give them, but they must sum perfectly to one. The program will throw an explicit error if this is not the case.

---
The contents of this repository are distributed under the generic [MIT License](./LICENSE).

This program is maintained by Matt Youngberg. Feel free to email him with any issues at [matt_youngberg@outlook.com](mailto:matt_youngberg@outlook.com)
