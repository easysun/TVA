use anchor_lang::prelude::*;

declare_id!("TVA111111111111111111111111111111111111111");

#[program]
pub mod time_authority {
    use super::*;

    pub fn initialize(ctx: Context<Initialize>) -> Result<()> {
        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize {}