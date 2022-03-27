
function glsrequest(){
  ethereum.request({
      method: 'wallet_watchAsset',
      params: {
        type: 'ERC20',
        options: {
          address: '0x3ffd098e99f5e0f4b2f73d6ad1ee6552e880d7f5',
          symbol: 'GLS',
          decimals: 18,
          image: 'https://gateway.pinata.cloud/ipfs/Qmb1WF49LsMJuuTmvufXpGtqdw1P7SVFJ6eSnQyRufb5RP',
        },
      },
    }).then((success) => {
        if (success) {
          console.log('GLS successfully added to wallet!')
        } else {
          throw new Error('Something went wrong.')
        }
      })
      .catch(console.error)}